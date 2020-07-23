function addTagsLoop(jsonData, parentId) {
    "use strict";
    for (var key in jsonData) {
        var newTag = document.createElement(jsonData[key].tagName);

        for (var attribute in jsonData[key]) {
            if (attribute != 'tagName' && attribute != 'children') {
                newTag[attribute] = jsonData[key][attribute];
            };
        };

        if (parentId !== false) {
            document.getElementById(parentId).appendChild(newTag);
        } else {
            document.body.appendChild(newTag);
        }

        if (jsonData[key].hasOwnProperty('children')) {
            addTagsLoop(jsonData[key].children, jsonData[key].id);
        }
    }
}

window.onload = function() {
    addTagsLoop(json.html.body, false);
};