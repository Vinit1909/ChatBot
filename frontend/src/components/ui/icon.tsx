import React from 'react';
import companyLogo from './companyLogo.png';

interface HeaderProps {
    companyName: string;
}

const Header: React.FC<HeaderProps> = ({ companyName }) => {
    const headerStyle = {
        display: 'flex',
        alignItems: 'center',
        fontSize: '30px',
        fontFamily: 'Jaturat',
    };

    const logoStyle = {
        height: '3em',
        // marginRight: '5px',
    };

    return (
        <div className="header" style={headerStyle}>
            <div className="logo">
                <img src={companyLogo} alt="Company Logo" style={logoStyle} />
            </div>
            <div className="company-name">
                {companyName}
            </div>
        </div>
    );
};

interface CardProps {
    companyName: string;
}

const Card: React.FC<CardProps> = ({ companyName }) => {
    const cardStyle = {
        alignItems: 'center',
        border: '2px solid black',
        borderRadius: '30px',
        padding: '20px',
        boxShadow: '0 2px 6px rgba(0, 0, 0, 0.6)',
        maxWidth: '275px',
        margin: '10px auto',
    };

    return (
        <div style={cardStyle}>
            <Header companyName={companyName} />
        </div>
    );
};

export { Header, Card };
