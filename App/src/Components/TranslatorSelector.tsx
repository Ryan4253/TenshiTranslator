import React, {useState} from 'react';
import Box from '@mui/material/Box';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import Typography from '@mui/material/Typography';
const { ipcRenderer } = window.require('electron');

const TranslatorSelector = (props: {localTranslatorsAllowed: Boolean, setTranslator: (arg:string) => void}) =>   {
	const [translator, setTraslator] = React.useState("Online");

	const updateTranslator = (event: React.MouseEvent<HTMLElement, MouseEvent>, newTranslator: any) => {
		if (newTranslator === null) {
			return;
		}

		setTraslator(newTranslator);
		props.setTranslator(newTranslator)
		ipcRenderer.send('setTranslator', newTranslator);
	};

	return (
		<Box sx={{m:1}}>
			<Typography variant="h5">Translator</Typography>
			<ToggleButtonGroup
				exclusive 
				color="primary"
				aria-label="Translator Selection"
				value={translator}
				onChange={updateTranslator}
			>
				<ToggleButton value="Online">Online</ToggleButton>
				<ToggleButton value="Offline" disabled={!props.localTranslatorsAllowed}>Offline</ToggleButton>
				<ToggleButton value="Batch" disabled={!props.localTranslatorsAllowed}>Batch</ToggleButton>
			</ToggleButtonGroup>
		</Box>
	);
}

export default TranslatorSelector;