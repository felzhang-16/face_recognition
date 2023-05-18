
const askFolder = async () => {
    return await eel.ask_folder()();
};


const askFile = async (fileType) => {
    return await eel.ask_file(fileType)();
};


const doesFileExist = async (path) => {
    return await eel.does_file_exist(path)();
};


const doesFolderExist = async (path) => {
    return await eel.does_folder_exist(path)();
};


const doesFolderEmpty = async (path) => {
    return await eel.does_folder_empty(path)();
};