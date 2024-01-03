import React from 'react';
import Box from '@mui/material/Box';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import Typography  from '@mui/material/Typography';
const { ipcRenderer } = window.require('electron');

function OutputFormatSelector(){
	const [format, setFormat] = React.useState("LineByLine");

	const updateFormat = (event: React.MouseEvent<HTMLElement, MouseEvent>, newFormat: any) => {
		if(newFormat === null){
			return;
		}

		setFormat(newFormat);
		ipcRenderer.send('setFormat', newFormat);
	};

	return (
		<Box sx={{mt:1, mb:2}}>
            <Typography variant="h5">Format Selection</Typography>
            <ToggleButtonGroup 
                exclusive 
                color="primary"
                value={format}
                onChange={updateFormat}
            >
                <ToggleButton value="LineByLine">Line By Line</ToggleButton>
                <ToggleButton value="EnglishOnly">English Only</ToggleButton>
            </ToggleButtonGroup>
		</Box>
	);
}

export default OutputFormatSelector;