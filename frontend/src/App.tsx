import { Routes, Route } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { apiClient } from "./api/client";

function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-slate-100">
      <div className="mx-auto max-w-4xl px-6 py-16">
        <header className="mb-12">
          <h1 className="text-4xl font-bold text-slate-900">
            AP CSA Practice
          </h1>
          <p className="mt-2 text-lg text-slate-600">
            Past exam MCQs & FRQ autograder - built for serious learners.
          </p>
        </header>

        <div className="grid gap-4 sm:grid-cols-2">
          <Card title="MCQ Practice" subtitle="Coming in Phase 1.3" disabled />
          <Card title="FRQ Autograder" subtitle="Coming in Phase 1.4" disabled/>
        </div>

        <div className="mt-12">
          <HealthBadge />
        </div>
      </div>
    </div>
  );
}

function Card({
  title,
  subtitle,
  disabled,
}: {
  title: string;
  subtitle: string;
  disabled?: boolean;
}) {
  return (
    <div 
      className={`rounded-lg border bg-white p-6 shadow-sm ${
        disabled ? "border-slate-200 opacity-60" : "border-slate-300"
      }`}
    >
      <h2 className="text-lg font-semibold text-slate-900">{title}</h2>
      <p className="mt-1 text-sm text-slate-500">{subtitle}</p>
    </div>
  );
}

function HealthBadge() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["health"],
    queryFn: async () => {
      const res = await apiClient.get("/health");
      return res.data;
    },
  });

  if (isLoading) return <Badge color="gray" label="Connecting to backend..." />;
  if (error)
    return (
      <Badge 
        color="red"
        label="Backend unreachable - is uvicorn running on :8000?"
      />
  );
  return <Badge color="green" label={`Backend OK (env=${data.env})`} />;
}


function Badge({
  color,
  label,
}: {
  color: "green" | "red" | "gray";
  label: string;
}) {
  const cls = {
    green: "bg-green-100 text-green-800 border-green-300",
    red: "bg-red-100 text-red-800 border-red-300",
    gray: "bg-slate-100 text-slate-700 border-slate-300",
  }[color];

  return (
    <span className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-medium ${cls}`}>
      {label}
    </span>
  );
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
    </Routes>
  )
}
  

export default App
