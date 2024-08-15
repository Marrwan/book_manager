import axios from 'axios';
import { toast } from 'react-toastify';

const API_URL = process.env.API_URL || 'http://localhost:8000/api/books';
const handleError = (error, defaultMessage) => {
    const errorMessage = error.response?.data?.message || defaultMessage;
    console.error(errorMessage);
    toast.error(errorMessage);
};

export const getBooks = () => {
    return axios.get(API_URL)
        .then(res => {
            if (res.data.success) {
                return res.data.data;
            } else {
                toast.error(res.data.message);
                return [];
            }
        })
        .catch(error => handleError(error, 'Failed to fetch books.'));
};

export const getBook = (id) => {
    return axios.get(`${API_URL}/${id}`)
        .then(res => {
            if (res.data.success) {
                return res.data.data;
            } else {
                toast.error(res.data.message);
                return null;
            }
        })
        .catch(error => handleError(error, 'Failed to fetch book.'));
};

export const addBook = (book) => {
    return axios.post(API_URL, book)
        .then(res => {
            if (res.data.success) {
                toast.success('Book added successfully!');
                return res.data.data;
            } else {
                toast.error(res.data.message);
            }
        })
        .catch(error => handleError(error, 'Failed to add book.'));
};

export const updateBook = (id, book) => {
    return axios.put(`${API_URL}/${id}`, book)
        .then(res => {
            if (res.data.success) {
                toast.success('Book updated successfully!');
                return res.data.data;
            } else {
                toast.error(res.data.message);
            }
        })
        .catch(error => handleError(error, 'Failed to update book.'));
};

export const deleteBook = (id) => {
    return axios.delete(`${API_URL}/${id}`)
        .then(res => {
            console.log({res, data: res.data});
            if (res.data.success) {
                toast.success('Book deleted successfully!');
            } else {
                toast.error(res.data.message);
            }
        })
        .catch(error => handleError(error, 'Failed to delete book.'));
};
