import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Button, Card, CardContent, Container, Grid, Typography } from '@mui/material';
import BookList from '../components/BookList';
import {deleteBook, getBooks} from "../api/bookAPi";

const HomePage = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        getBooks().then(setBooks);
    }, []);

    const handleDelete = (id) => {
        deleteBook(id).then(() => setBooks(books.filter((book) => book.id !== id)));
    };

    return (
        <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Typography variant="h1" gutterBottom align="center">
                Book Manager
            </Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} md={6}>
                    <Card>
                        <CardContent>
                            <Typography variant="h5">Manage Your Books</Typography>
                            <Button
                                component={Link}
                                to="/add"
                                variant="contained"
                                color="primary"
                                sx={{ mt: 2 }}
                            >
                                Add New Book
                            </Button>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={12}>
                    <BookList books={books} onDelete={handleDelete} />
                </Grid>
            </Grid>
        </Container>
    );
};

export default HomePage;
