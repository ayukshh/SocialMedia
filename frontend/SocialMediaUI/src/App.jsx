import Home from './home.jsx';
import Profile from './profile.jsx';
import Register from './register.jsx';
import Login from './login.jsx';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './layout.jsx';
import Posts from './posts.jsx';


function App() {
  return (
    <Router>
      <Routes>
        {/* Routes that share the Layout (navbar, etc.) */}
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/home" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
        </Route>

        {/* Routes that DON'T use the Layout */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path='/posts' element={<Posts/>} />


      </Routes>
    </Router>
  );
}

export default App;