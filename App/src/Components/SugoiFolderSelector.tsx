import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import {useState} from 'react';
import { IpcRendererEvent } from 'electron';
const { ipcRenderer } = window.require('electron');

const SugoiFolderSelector = (props: {setSelectionState: Function}) =>   {
	const [sugoiDirectory, selectSugoiDirectory] = useState('');
	
	const setSugoiDirectory = () => {
		ipcRenderer.send('setSugoiDirectory');
		ipcRenderer.once('sugoiDirectoryResult', (event: IpcRendererEvent, result: string) => {
		  	if (result && result.length > 0) {
				selectSugoiDirectory(result);
				props.setSelectionState();
		  	}
		});
	};

	return (
		<Box width="300px" height="120px" display="flex" flexDirection="column" alignItems="center">
		  	<Button variant="contained" onClick={setSugoiDirectory} sx={{m: 1}}>
				Select Sugoi Folder
		  	</Button>
		  	{sugoiDirectory && <Typography variant="caption" align="center">Sugoi Folder: {sugoiDirectory}</Typography>}
		</Box>
	);
}

export default SugoiFolderSelector