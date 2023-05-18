const folderSearch = async (elementId) => {
    const element = document.getElementById(elementId);
    const value = await askFolder();
    if (value !== null) {
        element.value = value;
    }
};


const fileSearch = async (elementId, file_type) => {
    const element = document.getElementById(elementId);
    const value = await askFile(file_type);
    if (value !== null) {
        element.value = value;
    }
};


const recognitionScript = async (event) => {
    if (recognizingState === RECOGNIZING_STATE_RECOGNIZING) {
        return;
    }
    if (recognizingState === RECOGNIZING_STATE_COMPLETE) {
        setRecognizingState(RECOGNIZING_STATE_READY);
        return;
    }
    var config = getConfiguration();
    for (item in config) {
        if (config[item] == '') {
            alert('输入框为空，请重新输入');
            return;
        }
        if (item == "compare") {
            for (interItem in config[item]) {
                if (config[item][interItem] == '') {
                    alert('输入框为空，请重新输入');
                    return;
                }
            }
        }
    }
    startRecognizing(getConfiguration());

}


const setupEvents = () => {
    document.getElementById('input-source-dir').addEventListener('input', inputSourceDirChange);
    document.getElementById('input-destination-dir').addEventListener('input', inputDestinationDirChange);
    document.getElementById('input-source-dir-search').addEventListener('click', function () { folderSearch('input-source-dir'); });
    document.getElementById('input-destination-dir-search').addEventListener('click', function () { folderSearch('input-destination-dir'); });
    document.getElementById('input-compare-image-search').addEventListener('click', function () { fileSearch('input-compare-image', 'jpg'); });
    document.getElementById('button-start-recognition').addEventListener('click', recognitionScript);
}
