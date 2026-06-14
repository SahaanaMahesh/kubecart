import { useState } from "react";

export default function Chatbot() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    try {
      const res = await fetch("http://localhost:9000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      if (!res.ok) throw new Error("Chat failed");
      const data = await res.json();
      setResponse(data.response || "No response returned.");
    } catch (err) {
      setResponse("Unable to reach chatbot service right now.");
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Chatbot</h2>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <p>{response}</p>
    </div>
  );
}