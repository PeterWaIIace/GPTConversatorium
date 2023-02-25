const {useState,useEffect} = React;

let personalities = {"A":"","B":""};
let names = {"A":"PersonA","B":"PersonB"};

function Names()
{
    const [displayName1,  setDisplayName1] = useState("PersonA");
    const [displayName2,  setDisplayName2] = useState("PersonB");

    const handleName1 = event => {
        // 👇️ access textarea value
        setDisplayName2(event.target.value);
        names["A"] = event.target.value;
    };

    const handleName2 = event => {
        // 👇️ access textarea value
        setDisplayName1(event.target.value);
        names["B"] = event.target.value;
    };

    return (
        <div className="row">
            <div className="col-6">
                <div className="form-outline">
                    <textarea className="form-control" id="displayName1" rows="1" onChange={handleName1} style={{ background: 'rgba(10,0,0,.2)'}} value={displayName1}></textarea>
                </div>
            </div>
            <div className="col-6">
                <div className="form-outline">
                    <textarea className="form-control" id="displayName2" rows="1" onChange={handleName2} style={{ background: 'rgba(10,0,0,.2)'}} value={displayName2}></textarea>
                </div>
            </div>
        </div>
    );
};


function Personalities()
{
    const [displayPersonality1,  setDisplayPersonality1] = useState("");
    const [displayPersonality2,  setDisplayPersonality2] = useState("");

    const handlePersonality1 = event => {
        // 👇️ access textarea value
        setDisplayPersonality1(event.target.value);
        personalities["A"] = event.target.value;
    };

    const handlePersonality2 = event => {
        // 👇️ access textarea value
        setDisplayPersonality2(event.target.value);
        personalities["B"] = event.target.value;
    };

    return (
        <div className="row">
            <div className="col-6">
                <div className="form-outline">
                    <textarea className="form-control" id="displayPersonality1" rows="2" onChange={handlePersonality1} style={{ background: 'rgba(10,0,0,.5)'}} value={displayPersonality1}></textarea>
                </div>
            </div>
            <div className="col-6">
                <div className="form-outline">
                    <textarea className="form-control" id="displayPersonality2" rows="2" onChange={handlePersonality2} style={{ background: 'rgba(10,0,0,.5)'}} value={displayPersonality2}></textarea>
                </div>
            </div>
        </div>
    );
};


function Controls()
{
    const onStart = event => {
        fetch(`${window.location.origin}/buttons/start`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                  },
                body: JSON.stringify({
                    "A":personalities["A"],
                    "B":personalities["B"],
                    "NameA":names["A"],
                    "NameB":names["B"],
                })
            }
        ).catch(error   => console.error('Error:', error));
    }

    const onStop = event => {
        fetch(`${window.location.origin}/buttons/stop`,
            {
                method: 'POST'
            }
        ).catch(error   => console.error('Error:', error));
    }

    return (
        <div className="row">
            <div className="col-6" align="right">
                <button onClick={onStart} className="btn btn-primary m-1 mt-2 col-4" title="Start">Start</button>
            </div>
            <div className="col-6" align="left">
                <button onClick={onStop} className="btn btn-primary m-1 mt-2 col-4" title="Stop">Stop</button>
            </div>
        </div>
    )
};

function Dialog()
{
    const [conversation, updateConversation]   = useState("");

    setInterval(function() {
        fetch(`${window.location.origin}/readConversation`)
        .then(response => response.text())
        .then(text     => updateConversation(text))
        .catch(error   => console.error('Error:', error));
    }, 1000);

    return (
        <div className="col">
            <ul dangerouslySetInnerHTML={{__html: conversation }}/>
        </div>
    );
};


ReactDOM.render(
    <div className="container">
        <div className="row">
            <div className="col" align="center">
                <h1>GPT Conversatorium</h1>
            </div>
        </div>
        <div className="row">
            <div className="col-sm">
                <Names></Names>
                <Personalities></Personalities>
                <Controls></Controls>
            </div>
        </div>
        <div className="row">
            <Dialog></Dialog>
        </div>
    </div>
    ,document.getElementById('root')
);
