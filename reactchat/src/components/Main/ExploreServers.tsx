import {List,ListItem,ListItemButton,ListItemIcon,ListItemText,Box,Typography,} from '@mui/material';
import useCrud from '../../hooks/useCrud';
import { useEffect } from 'react';
import ListItemAvatar from '@mui/material/Avatar';
import Avatar from '@mui/material/Avatar';
import { MEDIA_URL } from '../../config';
import {Link, useParams} from 'react-router-dom';

interface Server {
    id: number;
    name: string;
    category: string;
    icon: string;
}

const ExploreServers = () => {
    const { categoryName } = useParams();
    const url = categoryName ? `/server/select/?category=${categoryName}` : "/sever/select"
    const { dataCRUD, fetchData } = useCrud<Server>([], url);

    return (
    <div></div>
    )
}

export default ExploreServers