import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./App.css";

import Home from "./pages/Home";
import Products from "./pages/Products";
import Orders from "./pages/Orders";
import Reviews from "./pages/Reviews";
import Chatbot from "./pages/Chatbot";

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <nav className="navbar">
          <h1>🌿 KubeCart</h1>

          <div className="nav-links">
            <Link to="/">🏠 Home</Link>
            <Link to="/products">🛍 Products</Link>
            <Link to="/orders">📦 Orders</Link>
            <Link to="/reviews">⭐ Reviews</Link>
            <Link to="/chatbot">🤖 Chatbot</Link>
          </div>
        </nav>

        <main className="main-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/products" element={<Products />} />
            <Route path="/orders" element={<Orders />} />
            <Route path="/reviews" element={<Reviews />} />
            <Route path="/chatbot" element={<Chatbot />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;