import Image from 'next/image';

export default function Roster(data) {
  const { name, position, team, stats, image } = data;

  return (
    <div>
      <Image src={image} alt={name} width="100" height="100" layout="responsive"/>
    </div>
  );
}