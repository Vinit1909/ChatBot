import { useEffect } from "react";

import { useChatSession } from "@chainlit/react-client";
import { Playground } from "./components/playground";
import { Card } from "@/components/ui/icon"

const CHAINLIT_SERVER = "http://localhost:8000";
const userEnv = {};

function App() {
  const { connect } = useChatSession();

  useEffect(() => {
    connect({ wsEndpoint: CHAINLIT_SERVER, userEnv });
  }, [connect]);

  const fixedCardStyle = {
    position: 'fixed',
    alignItems: 'center',
    // top: '20px',   
    left: '50%',
    transform: 'translateX(-50%)',
    zIndex: 1000,
    width: 1600,
    borderRadius: '30px',
  };

  return (
    <>
      <div className="w-100 h-40 bg-gray-100" style={fixedCardStyle}>
        <Card companyName="ARMONY" />
      </div>
      <div>
        <Playground />
      </div>
    </>
  );
}

export default App;
