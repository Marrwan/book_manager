import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import HomePage from './pages/HomePage';
import AddBookPage from './pages/AddBookPage';
import EditBookPage from './pages/EditBookPage';

function App() {
    return (
        <Router>
            <ToastContainer position="top-right" autoClose={3000} />
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/add" element={<AddBookPage />} />
                <Route path="/edit/:id" element={<EditBookPage />} />
            </Routes>
        </Router>
    );
}

export default App;
