async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const message = inputField.value;
    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user-message">You: ${message}</div>`;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    });

    const data = await response.json();

    chatBox.innerHTML += `<div class="bot-message">Bot: ${data.response}</div>`;

    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}
