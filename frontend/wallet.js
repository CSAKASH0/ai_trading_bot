async function connectWallet() {
    if (window.ethereum) {
        const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
        const address = accounts[0];
        document.getElementById("wallet-status").innerText = `Connected: ${address}`;
    } else {
        alert("MetaMask not found. Please install MetaMask browser extension.");
    }
}

async function checkBalance() {
    const wallet = document.getElementById("wallet-address").value;
    const res = await fetch(`/api/balance/${wallet}`);
    const data = await res.json();
    document.getElementById("balance-result").innerText = `Balance: ${data.balance} ETH`;
}

async function uploadChart() {
    const fileInput = document.getElementById("chart-upload");
    const file = fileInput.files[0];
    if (!file) return alert("Please select a chart image to upload");

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch('/api/trend', {
        method: 'POST',
        body: formData
    });

    const result = await res.json();
    document.getElementById("trend-result").innerText = `Trend: ${result.trend} (Confidence: ${result.confidence})`;
}

async function getSignal() {
    const symbol = document.getElementById("symbol-input").value;
    const res = await fetch('/api/signal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symbol })
    });

    const data = await res.json();
    document.getElementById("signal-result").innerText = `Signal: ${data.signal}`;
}
