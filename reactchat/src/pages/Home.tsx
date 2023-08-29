import {Box, CssBaseline} from '@mui/material';
import PrimaryAppBar from './PrimaryAppBar';


const Home = () => {
    return (
    <Box sx={{display:'flex'}}>
        <CssBaseline />
        <PrimaryAppBar />
    </Box>
    );
};

export default Home;