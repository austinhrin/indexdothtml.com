var json = {
    "html": {
        "body": [{
            "tagName": "h1",
            "class": "header",
            "id": "header",
            "innerHTML": "Hello World!"
        }, {
            "name": "subHeader",
            "tagName": "h3",
            "class": "subHeader",
            "id": "subHeader",
            "innerHTML": "Hello World! 2"
        }, {
            "name": "paragraph",
            "tagName": "p",
            "class": "paragraph",
            "id": "paragraph",
            "innerHTML": "Hello World! 3"
        }, {
            "name": "div1",
            "tagName": "div",
            "class": "div1",
            "id": "div1",
            "innerHTML": "",
            "children": [{
                "name": "div1InsideOfDiv1",
                "tagName": "div",
                "class": "div1InsideOfDiv1",
                "id": "div1InsideOfDiv1",
                "innerHTML": "",
                "children": [{
                    "name": "paragraph1",
                    "tagName": "p",
                    "class": "paragraph",
                    "innerHTML": "I am paragraph 1."
                }, {
                    "name": "paragraph2",
                    "tagName": "p",
                    "class": "paragraph",
                    "id": "paragraph",
                    "innerHTML": "I am paragraph 2."
                }, {
                    "name": "paragraph3",
                    "tagName": "p",
                    "id": "paragraph",
                    "innerHTML": "I am paragraph 3."
                }, {
                    "name": "divx",
                    "tagName": "div",
                    "id": "divx",
                    "children": [{
                        "name": "divy",
                        "tagName": "div",
                        "id": "divy",
                        "children": [{
                            "name": "divz",
                            "tagName": "div",
                            "id": "divz",
                            "children": [{
                                "name": "paragraph",
                                "tagName": "p",
                                "innerHTML": "I am in divz that is in divy that is in divx that is in div1InsideOfDiv1 that is in div1. :D"
                            }]
                        }]
                    }]
                }]
            }, {
                "name": "div2InsideOfDiv1",
                "tagName": "div",
                "class": "div2InsideOfDiv1",
                "id": "div2InsideOfDiv1",
                "innerHTML": "",
                "children": [{
                    "name": "paragraph1",
                    "tagName": "p",
                    "class": "paragraph",
                    "id": "paragraph",
                    "innerHTML": "I am paragraph 1 in div2InsideOfDiv1 that is in div1."
                }, {
                    "name": "paragraph2",
                    "tagName": "p",
                    "class": "paragraph",
                    "id": "paragraph",
                    "innerHTML": "I am paragraph 2 in div2InsideOfDiv1 that is in div1."
                }]
            }]
        }]
    }
};