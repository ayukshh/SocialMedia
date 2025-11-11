import api from './api.js';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './auth.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const res = await api.post('/auth/login', { username, password });

      // Save token and redirect
      localStorage.setItem('token', res.data.access_token);
      navigate('/');
    } catch (err) {
      const detail =
        err?.response?.data?.detail ||
        (typeof err?.response?.data === 'string' ? err.response.data : null) ||
        err?.message ||
        'Login failed. Please check your credentials.';
      setError(detail);
    }
  };

  return (
    <div className="auth-container">
      <form onSubmit={handleSubmit} className="auth-form">
        <h2>Login</h2>
        
        {error && <p className="error">{error}</p>}
        
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          required
        />
        
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          required
        />
        
        <button type="submit">Login</button>
        
        <p>
          Don't have an account ? <Link to="/register">Register</Link>
        </p>
      </form>
    </div>
  );
}

export default Login;