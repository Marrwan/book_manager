import React from 'react';
import { Button, TextField, Grid } from '@mui/material';

const BookForm = ({ book = {}, onSubmit }) => {
    const [title, setTitle] = React.useState(book.title || '');
    const [author, setAuthor] = React.useState(book.author || '');
    const [isbn, setIsbn] = React.useState(book.isbn || '');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ title, author, isbn });
    };

    return (
        <form onSubmit={handleSubmit}>
            <Grid container spacing={3}>
                <Grid item xs={12}>
                    <TextField
                        label="Title"
                        variant="outlined"
                        fullWidth
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        label="Author"
                        variant="outlined"
                        fullWidth
                        value={author}
                        onChange={(e) => setAuthor(e.target.value)}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        label="ISBN"
                        variant="outlined"
                        fullWidth
                        value={isbn}
                        onChange={(e) => setIsbn(e.target.value)}
                        required
                    />
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" color="primary" type="submit">
                        {book.id ? 'Update Book' : 'Add Book'}
                    </Button>
                </Grid>
            </Grid>
        </form>
    );
};

export default BookForm;
