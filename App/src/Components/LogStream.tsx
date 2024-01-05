import { useState, useEffect, useRef, Fragment } from 'react';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
const { ipcRenderer } = window.require('electron');

const LogStream = () =>{
  const [textStream, setTextStream] = useState<string[]>([]);
  const paperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleTextStream = (event: any, text: string) => {
        setTextStream((prevTextStream) => [...prevTextStream, text]);

        setTimeout(() => {
            if (paperRef.current) {
                paperRef.current.scrollTop = paperRef.current.scrollHeight;
            }
        }, 5);
    };

    ipcRenderer.on('translationProcess', handleTextStream);

    return () => {
      ipcRenderer.removeListener('translationProcess', handleTextStream);
    };
  }, []);

    return (
        <Paper ref={paperRef} elevation={3} sx={{width:"100vh", height:"30vh", backgroundColor:"#403e41", overflowY:"auto", p: 1, m:1}}>
            <Typography variant="h6" color="white" textAlign="left">Logs</Typography>
            {textStream.map((text, index) => (
                (text === '') ? index === textStream.length - 1 ? 
                <div></div>: 
                <Typography textAlign="left" dangerouslySetInnerHTML={{ __html: '&nbsp;' }} />:
                <Typography textAlign="left" color="white">{text}</Typography>
            ))}
        </Paper>
    );
}

export default LogStream;