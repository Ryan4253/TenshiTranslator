import React, {useState} from 'react';
import './App.css';

import Button from '@mui/material/Button';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';   
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import Tooltip from '@mui/material/Tooltip';
import HelpIcon from '@mui/icons-material/Help';

const { ipcRenderer } = window.require('electron');

function BatchSizeSlider() {
  	const marks = [
		{value: 2},
		{value: 4},
		{value: 8},
		{value: 16},
		{value: 32},
		{value: 64},
		{value: 128},
		{value: 256}
  	];

	const [batchSize, setBatchSize] = useState(64);

	const updateBatchSize = (event: Event, newBatchSize: number | number[]) => {
		setBatchSize(newBatchSize as number);
		ipcRenderer.send('setBatchSize', newBatchSize);
	};

	return (
		<div>
		<Box display="flex" justifyContent="center" alignItems="center">
			<body>Batch Size&nbsp;</body> 
			<Tooltip title="Temp" placement="right">
			<HelpIcon />
			</Tooltip>
		</Box>
		<Slider
			defaultValue={batchSize}
			step={null}
			valueLabelDisplay="auto"
			onChange={updateBatchSize}
			marks={marks}
			min={2}
			max={256}
		/>
		</div>
	);
}

function TimeoutSlider() {
	const [timeout, setTimeout] = useState(315);

	const updateTimeout = (event: Event, newTimeout: number | number[]) => {
		setTimeout(newTimeout as number);
		ipcRenderer.send('setTimeout', newTimeout);
	};

	return (
		<div>
		<Box display="flex" justifyContent="center" alignItems="center">
			<body>Timeout Wait&nbsp;</body> 
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

function TranslatorSelection() {
	const [translator, setTraslator] = React.useState("Online");

	const updateTranslator = (event: React.MouseEvent<HTMLElement, MouseEvent>, newTranslator: any) => {
		if (newTranslator === null) {
		return;
		}

		setTraslator(newTranslator);
		ipcRenderer.send('setTranslator', newTranslator);
	};

	return (
		<Box height={165} width="12%" alignItems="center" justifyContent="center">
		<body>Translator</body>
		<ToggleButtonGroup 
			exclusive 
			color="primary"
			aria-label="Translator Selection"
			value={translator}
			onChange={updateTranslator}
		>
			<ToggleButton value="Online">Online</ToggleButton>
			<ToggleButton value="Offline">Offline</ToggleButton>
			<ToggleButton value="Batch">Batch</ToggleButton>
		</ToggleButtonGroup>

		<br></br>

		{translator === "Batch" && <BatchSizeSlider />}
		{translator === "Online" && <TimeoutSlider />}
		</Box>
		);
}

function OutputFormatSelection(){
	const [format, setFormat] = React.useState("LineByLine");

	const updateFormat = (event: React.MouseEvent<HTMLElement, MouseEvent>, newFormat: any) => {
		if(newFormat === null){
		return;
		}

		setFormat(newFormat);
		ipcRenderer.send('setFormat', newFormat);
	};

	return (
		<Box>
		<body>Format Selection</body>
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

const TranslationButton = () => {
	const sendTranslationRequest = () => {
		ipcRenderer.send('translate');
	};

	return (
		<Button variant="contained" color="primary" onClick={sendTranslationRequest}>
		Translate
		</Button>
	);
};

function App() {
	return (
		<div className="App">
		<header className="App-header">
			<TranslatorSelection />
			<OutputFormatSelection />
			<TranslationButton />
		</header>
		</div>
	);
}

export default App;