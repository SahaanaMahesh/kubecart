import { useEffect, useState } from "react";

export default function Reviews() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("http://localhost:9000/reviews")
      .then((res) => res.json())
      .then((data) => setReviews(data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Reviews</h2>

      {reviews.map((r) => (
        <div key={r.id}>
          <h3>Review #{r.id}</h3>
          <p>Product ID: {r.product_id}</p>
          <p>Rating: ⭐ {r.rating}</p>
          <p>{r.comment}</p>
        </div>
      ))}
    </div>
  );
}