// Modules to control application life and create native browser window
import { app, BrowserWindow, ipcMain, IpcMainEvent, dialog } from 'electron'
import * as path from 'path'
import * as url from 'url'

let mainWindow : BrowserWindow | null;

const runIPC = () => {
	let translator = 'Online';
	let batchSize = 64;
	let format = 'LineByLine';
	let timeout = 315;
	let sugoiDirectory = 'C://';

	ipcMain.on('setSugoiDirectory', async (event: IpcMainEvent) => {
		const result = await dialog.showOpenDialog(mainWindow!, {
		  properties: ['openDirectory'],
		});

		sugoiDirectory = result.filePaths[0];
		console.log('Selected Sugoi Directory: ', sugoiDirectory)
		event.reply('sugoiDirectoryResult', sugoiDirectory);
	});

	ipcMain.on('setFormat', (event: IpcMainEvent, value: string) => {
		console.log('Format received in main process:', value);
		format = value;
	});
	
	ipcMain.on('setBatchSize', (event: IpcMainEvent, value: number) => {
		console.log('Slider value received in main process:', value);
		batchSize = value;
	});
	
	ipcMain.on('setTranslator', (event: IpcMainEvent, value: string) => {
		console.log('Translator received in main process:', value);
		translator = value;
	});
	
	ipcMain.on('setTimeout', (event: IpcMainEvent, value: number) => {
		console.log('Timeout received in main process:', value);
		timeout = value;
	});

	ipcMain.on('translate', (event: IpcMainEvent) => {
		const executablePath = path.join(__dirname, '..', '..', 'Backend', 'Backend.exe');
	
		const { spawn } = require('child_process');
		const child = spawn(executablePath, ['--TimeoutWait', timeout, '--BatchSize', batchSize, '--SugoiDirectory', sugoiDirectory, translator, format, 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Correction\\Names.csv', 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Correction\\Corrections.csv', 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\stuff.txt']);
		//, 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\test.txt'
	
		child.stdout.setEncoding('utf8');
		child.stdout.on('data', function(data : string) {
			console.log('stdout: ' + data);
		});
	
		child.stderr.setEncoding('utf8');
		child.stderr.on('data', function(data : string) {
			console.log('stderr: ' + data);
		});
	});	
}

function createWindow() {
	const startUrl = process.env.DEV 
					? 'http://localhost:3000'
					: url.format({ pathname: path.join(__dirname, '/../build/index.html'),
					protocol: 'file:',
					slashes: true});

	mainWindow = new BrowserWindow({
		show: false,
		webPreferences: {
			nodeIntegration: true,
			contextIsolation: false
		}
	});

	mainWindow.loadURL(startUrl);
	mainWindow.maximize();
	mainWindow.show();
	mainWindow.moveTop();
	
	mainWindow.on('closed', function() {
		mainWindow = null;
	});
}

app.whenReady().then(() => {
	createWindow();
	runIPC();

	app.on('activate', function () {
		if (BrowserWindow.getAllWindows().length === 0) {
			createWindow();
		}
	})
}).catch((e) => console.log(e));

app.on('window-all-closed', function () {
  	if (process.platform !== 'darwin') {
		app.quit();
	}
})