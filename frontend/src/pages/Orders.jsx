import { useEffect, useState } from "react";

export default function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch("http://localhost:9000/orders")
      .then((res) => {
        if (!res.ok) throw new Error("Failed to load orders");
        return res.json();
      })
      .then((data) => setOrders(Array.isArray(data) ? data : []))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Orders</h2>

      {orders.map((o) => (
        <div key={o.id}>
          <h3>Order #{o.id}</h3>
          <p>User: {o.user_id}</p>
          <p>Product ID: {o.product_id}</p>
          <p>Quantity: {o.quantity}</p>
          <p>Status: {o.status}</p>
        </div>
      ))}
    </div>
  );
}