import React from 'react';
import {Table, TableBody, TableCell, TableHead, TableRow, Button, Typography} from '@mui/material';
import { Link } from 'react-router-dom';

const BookList = ({ books, onDelete }) => {
    return (
        <Table>
            <TableHead>
                <TableRow>
                    <TableCell>Title</TableCell>
                    <TableCell>Author</TableCell>
                    <TableCell>ISBN</TableCell>
                    <TableCell>Actions</TableCell>
                </TableRow>
            </TableHead>
            <TableBody>
                {books && books.length > 0 ? (books.map((book) => (
                    <TableRow key={book.id}>
                        <TableCell>{book.title}</TableCell>
                        <TableCell>{book.author}</TableCell>
                        <TableCell>{book.isbn}</TableCell>
                        <TableCell>
                            <Button component={Link} to={`/edit/${book.id}`} variant="contained">
                                Edit
                            </Button>
                            <Button onClick={() => onDelete(book.id)} variant="contained" color="secondary">
                                Delete
                            </Button>
                        </TableCell>
                    </TableRow>
                ))):(
                    <TableRow>
                        <TableCell colSpan={4}>
                            <Typography variant="body1" align="center" color="textSecondary">
                                There are no books available. Create one na 😎
                            </Typography>
                        </TableCell>
                    </TableRow>
                )}
            </TableBody>
        </Table>
    );
};

export default BookList;
