import { useState, useEffect } from "react";
import "./profile.css"

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data))
      .catch(err => console.error(err));
  }, [userId]);

 if (!user) {
  return <p>Loading...</p>;
}

return (
  <div>
    <div className="info-profile">
      <h2>username: {user.name}</h2>
      <h2>email: {user.email}</h2>
    </div>

    <div className="posts">
      <h2>Recent Posts</h2>
    </div>
  </div>
);
}

export default UserProfile;
