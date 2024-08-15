import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Container, Typography, Card, CardContent } from '@mui/material';
import BookForm from '../components/BookForm';
import {getBook, updateBook} from "../api/bookAPi";
const EditBookPage = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [book, setBook] = useState(null);

    useEffect(() => {
        getBook(id).then(setBook);
    }, [id]);

    const handleUpdateBook = (updatedBook) => {
        updateBook(id, updatedBook).then(() => navigate('/'));
    };

    if (!book) return navigate('/');

    return (
        <Container maxWidth="sm" sx={{ mt: 4 }}>
            <Typography variant="h2" gutterBottom align="center">
                Edit Book
            </Typography>
            <Card>
                <CardContent>
                    <BookForm book={book} onSubmit={handleUpdateBook} />
                </CardContent>
            </Card>
        </Container>
    );
};

export default EditBookPage;
