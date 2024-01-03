import {useState} from 'react';
import Box from '@mui/material/Box';   
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
import HelpIcon from '@mui/icons-material/Help';
const { ipcRenderer } = window.require('electron');

const TimeoutSlider = (props: {isVisible: Boolean}) =>  {
    const [timeout, setTimeout] = useState(315);

	const updateTimeout = (event: Event, newTimeout: number | number[]) => {
		setTimeout(newTimeout as number);
		ipcRenderer.send('setTimeout', newTimeout);
	};

    if(!props.isVisible) {
        return (<div></div>);
    }

	return (
		<div>
		<Box display="flex" justifyContent="center" alignItems="center">
			<Typography variant="h5">Timeout Wait</Typography> 
			<Tooltip title="Sugoi TL has a 5 min timeout after translation rate limit. Use this slider to set how long to wait before resuming." placement="right">
			<HelpIcon />
			</Tooltip>
		</Box> 
		<Slider
			defaultValue={timeout}
			step={5}
			valueLabelFormat={(value) => `${value} Seconds`}
			valueLabelDisplay="auto"
			onChange={updateTimeout}
			min={0}
			max={400}
		/>
		</div>
	);
}

export default TimeoutSlider;