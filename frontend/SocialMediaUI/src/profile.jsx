import { useState, useEffect } from "react";
import api from "./api.js";
import "./profile.css"

function UserProfile() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    setError("");
    api.get("/users/me")
      .then(res => setUser(res.data))
      .catch(err => {
        const detail = err?.response?.data?.detail || err?.message || "Failed to load profile";
        setError(detail);
      });
  }, []);

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  if (!user) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <div className="info-profile">
        <h2>username: {user.username}</h2>
        <h2>email: {user.email}</h2>
      </div>

      <div className="posts">
        <h2>Recent Posts</h2>
      </div>
    </div>
  );
}

export default UserProfile;
