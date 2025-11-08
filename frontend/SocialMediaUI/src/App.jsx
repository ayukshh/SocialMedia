import Home from './home.jsx';
import Profile from './profile.jsx';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './layout.jsx';


function App() {
  return (
     <Router>
      <Routes>
        {/* Wrap all routes that should share the same navbar in Layout */}
        <Route element={<Layout />}>
          <Route path="/" element={<Home/>} />
          <Route path="/home" element={<Home/>} />
          <Route path="/profile" element={<Profile />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;