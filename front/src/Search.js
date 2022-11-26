 
export default function Search() {
  return (
    <div className="p-6 max-w-xl mx-auto bg-white rounded-xl shadow-lg flex flex-col space-y-6">
      <h1 className="text-3xl text-center mx-auto">Find your basketball game</h1>
      <div className="flex items-center space-x-2">
        <input className="w-full py-3 pl-6 pr-2 text-gray-500 border rounded-md outline-none bg-gray-50 focus:bg-white focus:border-indigo-600" type="text" placeholder="localisation" />
        <input className="w-6/12 py-3 pl-6 pr-2 text-gray-500 border rounded-md outline-none bg-gray-50 focus:bg-white focus:border-indigo-600" type="date"></input>
        <button className="px-4 py-3 text-white bg-orange-600 border-l rounded ">
                    Search
        </button>
      </div>
    </div>
  );
}
