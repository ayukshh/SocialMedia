import React from "react";
import { useRef, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./navbar.css"; 

export default function Navbar() {
  const navigate = useNavigate();
  const [showNotifications, setShowNotifications] = useState(false);
 const [q, setQ] = useState("");
  const [users, setUsers] = useState([]);

  const handleLogoClick = () => {
    navigate("/home");
  };

  const handleProfileClick = () => {
    navigate("/profile");
  };

  function handleSearch(e) {
    e.preventDefault();
    fetch(`http://localhost:8000/users?q=${q}`)
      .then(res => res.json())
      .then(data => setUsers(data));
  }


  const handleNotificationsClick = () => {
    setShowNotifications(!showNotifications);
  };

  const closeNotifications = () => {
    setShowNotifications(false);
  };

  return (
    <>
      <nav className="navbar">
        <div className="navbar-left">
          <img 
            src="/images/argue2.jpg" 
            alt="Logo" 
            className="logo-image"
            onClick={handleLogoClick}
          />
          
        </div>
<div className="search-container">
  <form onSubmit={handleSearch} className="search-form">
    <input
      value={q}
      onChange={e => setQ(e.target.value)}
      placeholder="Search..."
      className="search-input"
    />
    <button type="submit" className="search-button">🔎</button>
  </form>

  <ul>
    {users.map(u => (
      <li key={u.id}>{u.name} - {u.email}</li>
    ))}
  </ul>
</div>

        <div className="navbar-right">
          {/* Clickable Notifications that opens popup */}
          <span 
            className="nav-item" 
            onClick={handleNotificationsClick}
          >
            Notifications
          </span>
          
          <span className="nav-item" onClick={handleProfileClick}>Profile</span>
        </div>
      </nav>

      {/* Notifications Popup */}
      {showNotifications && (
        <div className="popup-overlay" onClick={closeNotifications}>
          <div className="popup-content" onClick={(e) => e.stopPropagation()}>
            <div className="popup-header">
              <h3>Notifications</h3>
              <button className="close-btn" onClick={closeNotifications}>×</button>
            </div>
            <div className="popup-body">
              <div className="notification-item">
                <p>example notification</p>
                <span className="notification-time">2 min ago</span>
              </div>
            </div>
            <div className="popup-footer">
              <button className="mark-all-read">Mark all as read</button>
            </div>  
          </div>
        </div>
      )}
       
      <main>
      </main>
    </>
  );
}

