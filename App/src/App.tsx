import React, {useState} from 'react';
import './App.css';

import Box from '@mui/material/Box';   

import BatchSizeSlider from './Components/BatchSizeSlider';
import TimeoutSlider from './Components/TimeoutSlider';
import TranslatorSelector from './Components/TranslatorSelector';
import TranslateButton from './Components/TranslateButton';
import SugoiFolderSelector from './Components/SugoiFolderSelector';
import OutputFormatSelector from './Components/OutputFormatSelector';
import LogStream from './Components/LogStream';

function App() {
	let [localTranslatorAllowed, setLocalTranslatorAllowed] = useState(false);
	let [translator, setTranslator] = useState("Online");

	return (
		<div className="App">
			<SugoiFolderSelector setSelectionState={() => {setLocalTranslatorAllowed(true);}} />
			<Box width="30vh" height="170px" justifyContent="center" alignItems="center" textAlign="center" flexDirection={'column'}>
				<TranslatorSelector localTranslatorsAllowed={localTranslatorAllowed} 
									setTranslator={(translator: string) => {setTranslator(translator);}} />
				<BatchSizeSlider isVisible={translator === 'Batch'} />
				<TimeoutSlider isVisible={translator === 'Online'} />
			</Box>
			<OutputFormatSelector />
			<TranslateButton />
			<LogStream />
		</div>
	);
}

export default App;