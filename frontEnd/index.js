const {useState,useEffect} = React;

let personalities = {"A":"","B":""};

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
                <h3>Bot I:</h3>
                <div className="form-outline">
                    <textarea className="form-control" id="displayPersonality1" rows="2" onChange={handlePersonality1} style={{ background: 'rgba(10,0,0,.5)'}} value={displayPersonality1}></textarea>
                </div>
            </div>
            <div className="col-6">
                <h3>Bot II:</h3>
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
            <div className="col" align="left">
                <button onClick={onStart} className="btn btn-primary m-1 mt-2 col-4" title="Start">Start</button>
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
