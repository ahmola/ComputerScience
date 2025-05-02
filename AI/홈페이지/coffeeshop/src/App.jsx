import { Card, CardContent } from "@/components/ui/card";
import { useEffect, useState } from "react";
import axios from "axios";

const drinksAPI = "/api/drinks"; // REST API endpoint

export default function App() {
  const [drinks, setDrinks] = useState([]);

  useEffect(() => {
    axios.get(drinksAPI)
      .then(response => setDrinks(response.data))
      .catch(error => console.error("Failed to fetch drinks", error));
  }, []);

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6 p-6">
      {drinks.map((drink, index) => (
        <Card key={index} className="rounded-2xl shadow-lg">
          <img src={drink.imageUrl} alt={drink.name} className="w-full h-60 object-cover rounded-t-2xl" />
          <CardContent className="p-4">
            <h3 className="text-lg font-bold mb-2">{drink.name}</h3>
            <p className="text-sm text-gray-600 mb-1">{drink.description}</p>
            <span className="text-xs text-blue-600 font-semibold">{drink.type}</span>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}