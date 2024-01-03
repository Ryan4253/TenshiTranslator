import {useState} from 'react';
import Box from '@mui/material/Box';   
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
import HelpIcon from '@mui/icons-material/Help';
const { ipcRenderer } = window.require('electron');

const BatchSizeSlider = (props: {isVisible: Boolean}) =>  {
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

  if(!props.isVisible) {
    return (<div></div>);
  }

  return (
      <Box>
        <Box display="flex" justifyContent="center" alignItems="center">
            <Typography variant="h5">Batch Size</Typography>
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
      </Box>
  );
}

export default BatchSizeSlider;