let recognizingState = RECOGNIZING_STATE_READY;


const setRecognizingState = (newState) => {
    recognizingState = newState;

    const recognitionButton = document.getElementById('button-start-recognition');
    const outputSection = document.getElementById('output');
    const outputTextArea = outputSection.querySelector('textarea');
    const startButton = document.getElementById('button-start-recognition')

    switch (newState) {
        case RECOGNIZING_STATE_READY:
            recognitionButton.disabled = false;
            outputTextArea.value = '';
            outputTextArea.rows = 0;
            startButton.innerHTML = '开始';
            return;
        case RECOGNIZING_STATE_RECOGNIZING:
            recognitionButton.disabled = true;
            return;
        case RECOGNIZING_STATE_COMPLETE:
            recognitionButton.disabled = false;
            startButton.innerHTML = '清除输出';
            return;
    }

}

const startRecognizing = (config) => {
    eel.start_recognition(config)();
    setRecognizingState(RECOGNIZING_STATE_RECOGNIZING);
}

eel.expose(setRecognizingComplete);
function setRecognizingComplete(successful) {
    setRecognizingState(RECOGNIZING_STATE_COMPLETE);
}