import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './pages/Home';
import AboutUs from './pages/AboutUs';
import Predict from './pages/Predict';
import ContactUs from './pages/ContactUs';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-900 text-white">
        <nav className="bg-gray-800 p-4 text-yellow-400 flex justify-between items-center">
          <div className="text-2xl font-bold">Lawgorithm</div>
          <div className="flex space-x-6">
            <Link to="/" className="hover:text-yellow-300">Home</Link>
            <Link to="/about-us" className="hover:text-yellow-300">About Us</Link>
            <Link to="/predict" className="hover:text-yellow-300">Predict</Link>
            <Link to="/contact-us" className="hover:text-yellow-300">Contact Us</Link>
          </div>
        </nav>
        <div className="p-6">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about-us" element={<AboutUs />} />
            <Route path="/predict" element={<Predict />} />
            <Route path="/contact-us" element={<ContactUs />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
