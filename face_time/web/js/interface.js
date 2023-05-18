
const inputColour = async (inputNode, mustBeEmpty, allowedToBeFile, allowedToBeDirectory) => {
    const { value } = inputNode;
    if (
        (mustBeEmpty && await doesFolderEmpty(value))
        || (!mustBeEmpty && allowedToBeFile && await doesFileExist(value))
        || (!mustBeEmpty && allowedToBeDirectory && await doesFolderExist(value))
    ) {
        inputNode.style.border = "";
        return true;
    } else {
        inputNode.style.border = '1px solid rgb(244, 67, 54)';
        return false;
    }
};


const inputSourceDirChange = async (event) => {
    return inputColour(event.target, mustBeEmpty = false, allowedToBeFile = true, allowedToBeDirectory = true);
};

const inputSourceDirChangeWithTarget = async (target) => {
    return inputColour(target, mustBeEmpty = false, allowedToBeFile = true, allowedToBeDirectory = true);
};

const inputDestinationDirChange = async (event) => {
    return inputColour(event.target, mustBeEmpty = true, allowedToBeFile = false, allowedToBeDirectory = true);
};

const inputDestinationDirChangeWithTarget = async (target) => {
    return inputColour(target, mustBeEmpty = true, allowedToBeFile = false, allowedToBeDirectory = true);
};