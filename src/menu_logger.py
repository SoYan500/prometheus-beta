import logging
import os
from typing import Any, List, Optional

class MenuLogger:
    """
    A class to log user menu selections with configurable logging options.
    
    This logger provides functionality to track and record user interactions 
    with menus, supporting different logging levels and log file management.
    """
    
    def __init__(self, 
                 log_file: Optional[str] = None, 
                 log_level: int = logging.INFO):
        """
        Initialize the MenuLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. 
                                      If None, logs to console.
            log_level (int): Logging level from the logging module.
        """
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        # Configure logger
        self.logger = logging.getLogger('menu_logger')
        self.logger.setLevel(log_level)
        
        # Clear existing handlers to prevent duplicate logging
        self.logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler (if log_file is specified)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def log_selection(self, 
                      menu_name: str, 
                      selection: Any, 
                      user_id: Optional[str] = None) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Any): The selected item or option.
            user_id (Optional[str]): Optional user identifier.
        
        Raises:
            ValueError: If menu_name is empty.
        """
        # Validate input
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        # Prepare log message
        log_message = f"Menu: {menu_name}, Selection: {selection}"
        if user_id:
            log_message += f", User: {user_id}"
        
        # Log the selection
        self.logger.info(log_message)
    
    def get_log_entries(self, 
                        log_file: Optional[str] = None, 
                        max_entries: Optional[int] = None) -> List[str]:
        """
        Retrieve log entries from a log file.
        
        Args:
            log_file (Optional[str]): Path to the log file to read.
                                      If None, uses the current log file.
            max_entries (Optional[int]): Maximum number of entries to return.
        
        Returns:
            List[str]: List of log entries.
        """
        # If no log file specified, return empty list
        if not log_file:
            return []
        
        try:
            with open(log_file, 'r') as f:
                # Read all lines and optionally limit
                lines = f.readlines()
                
            # Slice to max_entries if specified
            if max_entries is not None:
                lines = lines[-max_entries:]
            
            return [line.strip() for line in lines]
        
        except FileNotFoundError:
            return []
        except IOError:
            self.logger.error(f"Could not read log file: {log_file}")
            return []