import Button from '@mui/material/Button';
const { ipcRenderer } = window.require('electron');

const TranslateButton = () => {
	const sendTranslationRequest = () => {
		ipcRenderer.send('translate');
	};

	return (
		<Button variant="contained" color="primary" onClick={sendTranslationRequest}>
			Translate
		</Button>
	);
};

export default TranslateButton;