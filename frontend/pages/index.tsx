import React from 'react';
import { useRecoilState } from 'recoil';
import { isLoggedInState } from '../states/authState';
import Header from '../components/Header';
import LoginPage from '../components/LoginPage';

const Home: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useRecoilState(isLoggedInState);

  return (
    <div>
      <Header />
      {!isLoggedIn && <LoginPage />}
    </div>
  );
};

export default Home;
