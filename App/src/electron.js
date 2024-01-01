// Modules to control application life and create native browser window
const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('node:path')

let translator = 'Online'
let batch_size = 64;
let format = 'LineByLine'
let timeout = 315;

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
	process.env.DEV && mainWindow.webContents.openDevTools();
	
	mainWindow.on('closed', function() {
		mainWindow = null;
	});
}

app.whenReady().then(() => {
	createWindow()

	app.on('activate', function () {
		if (BrowserWindow.getAllWindows().length === 0) createWindow()
	})
}).catch((e) => console.log(e));

app.on('window-all-closed', function () {
  	if (process.platform !== 'darwin') app.quit()
})


ipcMain.on('translate', (event) => {
    const executablePath = path.join(__dirname, '..', '..', 'Backend', 'Backend.exe');

    const { spawn } = require('child_process');
    console.log(batch_size);
    const child = spawn(executablePath, ['--TimeoutWait', timeout, '--BatchSize', batch_size, '--SugoiDirectory', 'C:\\Users\\ryanl\\Documents\\Apps\\Sugoi-Translator-Toolkit-6.0', translator, format, 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Correction\\Names.csv', 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\Correction\\Corrections.csv', 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\stuff.txt']).on('error', (error) => {
        console.log(error);
    });
    //, 'C:\\Users\\ryanl\\Desktop\\tenshi-translator\\sources\\test.txt'

    child.stdout.setEncoding('utf8');
    child.stdout.on('data', function(data) {
        console.log('stdout: ' + data);
    });

    child.stderr.setEncoding('utf8');
    child.stderr.on('data', function(data) {
        console.log('stderr: ' + data);
    });
});

ipcMain.on('setFormat', (event, value) => {
    console.log('Format received in main process:', value);
    format = value;
});

ipcMain.on('setBatchSize', (event, value) => {
	console.log('Slider value received in main process:', value);
	batch_size = value;
});

ipcMain.on('setTranslator', (event, value) => {
	console.log('Translator received in main process:', value);
	translator = value;
});

ipcMain.on('setTimeout', (event, value) => {
	console.log('Timeout received in main process:', value);
	timeout = value;
});