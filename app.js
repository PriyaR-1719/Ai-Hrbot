const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

const BACKEND_URL = "http://127.0.0.1:5000/chat"; // Flask backend endpoint

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});

function appendMessage(message, sender) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add(sender === "bot" ? "bot-message" : "user-message");
  msgDiv.textContent = message;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage(message, "user");
  userInput.value = "";

  const typingDiv = document.createElement("div");
  typingDiv.classList.add("bot-message");
  typingDiv.innerHTML = '<span class="typing"></span><span class="typing"></span><span class="typing"></span>';
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const response = await fetch(BACKEND_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: message }),
    });

    const data = await response.json();
    chatBox.removeChild(typingDiv);
    appendMessage(data.response || "Error: No response from server.", "bot");
  } catch (error) {
    chatBox.removeChild(typingDiv);
    appendMessage("⚠️ Error connecting to server.", "bot");
    console.error("Error:", error);
  }
}
