import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Typography, Card, CardContent } from '@mui/material';
import BookForm from '../components/BookForm';
import {addBook} from "../api/bookAPi";

const AddBookPage = () => {
    const navigate = useNavigate();

    const handleAddBook = (book) => {
        addBook(book).then(() => navigate('/'));
    };

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Typography variant="h2" gutterBottom align="center">
                Add Book
            </Typography>
            <Card>
                <CardContent>
                    <BookForm onSubmit={handleAddBook} />
                </CardContent>
            </Card>
        </Container>
    );
};

export default AddBookPage;
