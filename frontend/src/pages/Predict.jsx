function Predict() {
    return (
      <div className="min-h-screen p-10 bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto space-y-10">
          <h1 className="text-4xl font-bold text-yellow-300 text-center">
            Predict Case Outcome
          </h1>
          <p className="text-lg text-gray-400 text-center">
            Enter a summary of your case below to get a predicted win rate based on historical data and advanced machine learning models.
          </p>
          <div className="bg-gray-800 p-6 rounded-lg shadow-lg">
            <h2 className="text-2xl mb-4">Case Summary</h2>
            <textarea
              className="w-full p-4 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-300"
              rows="6"
              placeholder="Paste your case summary here..."
            ></textarea>
            <div className="flex justify-center mt-6">
              <button className="bg-yellow-400 text-gray-900 px-6 py-3 rounded-lg hover:bg-yellow-300 font-semibold">
                Predict Outcome
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
  
  export default Predict;
  