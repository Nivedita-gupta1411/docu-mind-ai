// src/components/Sidebar.jsx
import React from 'react';
import { NavLink } from 'react-router-dom';
import { Home, FileText, Upload, Search, MessageSquare, LayoutDashboard } from 'lucide-react';

const links = [
  { to: '/dashboard', label: 'Dashboard', icon: <LayoutDashboard className="w-5 h-5" /> },
  { to: '/documents', label: 'Documents', icon: <FileText className="w-5 h-5" /> },
  { to: '/upload', label: 'Upload', icon: <Upload className="w-5 h-5" /> },
  { to: '/search', label: 'Search', icon: <Search className="w-5 h-5" /> },
  { to: '/chat', label: 'AI Chat', icon: <MessageSquare className="w-5 h-5" /> },
];

export default function Sidebar() {
  return (
    <nav className="w-64 bg-white border-r border-gray-200 p-4 hidden md:block">
      <h2 className="text-xl font-semibold mb-6 flex items-center">
        <Home className="w-6 h-6 mr-2" /> Document AI
      </h2>
      <ul className="space-y-2">
        {links.map((link) => (
          <li key={link.to}>
            <NavLink
              to={link.to}
              className={({ isActive }) =>
                `flex items-center p-2 rounded-md hover:bg-gray-100 ${isActive ? 'bg-gray-200 font-medium' : ''}`
              }
            >
              {link.icon}
              <span className="ml-3">{link.label}</span>
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  );
}
