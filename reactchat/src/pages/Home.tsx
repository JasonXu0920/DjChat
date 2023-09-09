import {Box, CssBaseline} from '@mui/material';
import PrimaryAppBar from './PrimaryAppBar';
import PrimaryDraw from './PrimaryDraw';
import SecondaryDraw from './SecondaryDraw';
import Main from './Main';
import PopularChannels from '../components/PrimaryDraw/PopularChannels';


const Home = () => {
    return (
    <Box sx={{display:'flex'}}>
        <CssBaseline />
        <PrimaryAppBar />
        <PrimaryDraw>
            <PopularChannels/>
        </PrimaryDraw>
        <SecondaryDraw></SecondaryDraw>
        <Main></Main>
    </Box>
    );
};

export default Home;